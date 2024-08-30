#!/usr/bin/env python
'''
This script is used to get the camera setup for the telescope with given PREFIX.
This uses API of BH-TOM2.
This script also utilizes the .env file to get the API token. (dotenv library)
'''

import os
import requests
import argparse
import dotenv
import logging
import pandas as pd

__version__ = '0.1.0'

class BHTasks:

    def __init__(self, token):
        self.token = token

    def do_map(self):
        # obs = self.do_obs()
        logging.info(f"Generating map of the observatories.")
        
        return "Map generated."

    def do_cam(self, prefix=None):
        '''
        Get the camera setup for the telescope with given PREFIX.
        '''
        obs = self.do_obs()
        cameras = obs['cameras']

        if prefix:
            # Use list comprehension along with the next() function to find the first dictionary with the specified prefix
            matching_camera = next((camera_dict for camera in cameras for camera_dict in camera if camera_dict.get('prefix') == prefix), None)
            
            if matching_camera:
                logging.info(f"Matching dictionary found for the specified prefix: {prefix}")
            else:
                logging.error(f"No matching dictionary found for the specified prefix: {prefix}")
                exit()

            df_camera = pd.DataFrame(matching_camera, index=[0])
            return df_camera
        else:
            # Use explode to expand the list of dictionaries into separate rows
            df_expanded = cameras.to_frame().explode('cameras')
            # Use pd.json_normalize to flatten the dictionaries into columns
            flattened_df = pd.json_normalize(df_expanded['cameras'])
            cols_to_exclude = ['id', 'user', 'additional_info']
            all_cols = flattened_df.columns
            flattened_df.to_csv('cameras.csv', index=False, columns=[col for col in all_cols if col not in cols_to_exclude])
            return flattened_df

    def do_obs(self):
        '''
        Get the list of observatories.
        '''
        headers = {
            'Authorization': f'Token {self.token}',
            'Content-Type': 'application/json',
            'X-CSRFToken': 'uUz2fRnXhPuvD9YuuiDW9cD1LsajeaQnE4hwtEAfR00SgV9bD5HCe5i8n4m4KcOr',
            'accept': 'application/json'
        }

        api_url = f'https://bh-tom2.astrolabs.pl/observatory/getObservatoryList/'
        response = requests.post(api_url, headers=headers)
        if response.status_code != 200:
            logging.error(f"Error: {response.status_code}")
            exit()
        observatory_list = pd.json_normalize(response.json())
        if observatory_list['num_pages'][0] > 1:
            for page in range(2, observatory_list['num_pages']+1):
                response = requests.post(api_url, headers=headers, data={'page': page})
                if response.status_code != 200:
                    logging.error(f"Error: {response.status_code}")
                    exit()
                observatory_list = pd.concat([observatory_list, pd.json_normalize(response.json())], ignore_index=True)
        observatory_list = pd.DataFrame(observatory_list['data'][0])
        if args.task != 'cam':
            cols_to_exclude = ['id', 'comment', 'cameras']
            all_cols = observatory_list.columns
            observatory_list.to_csv('observatories.csv', index=False, columns=[col for col in all_cols if col not in cols_to_exclude])
        return observatory_list


    # for dynamically solving a job
    def solve_for(self, parser):
        do = "do_{name}".format(name=args.task)
        if hasattr(self, do) and callable(func := getattr(self, do)):
            if hasattr(args, 'prefix'):
                result = func(args.prefix)
            else:
                result = func()
            return result
        else:
            result = parser.print_help()
            exit()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='>> %(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S'
                        )
    dotenv.load_dotenv() # Load the .env file from the current directory

    parser = argparse.ArgumentParser(description='Use API of BH-TOM2 for different tasks.')
    # Global arguments
    parser.add_argument('--token', type=str, default=os.getenv('BHTOM_API_TOKEN'), help='Token for the API.')

    subparsers = parser.add_subparsers(help='Tasks: obs, cam, map', dest='task')

    # subparser for getting the observatory list
    parser_obs = subparsers.add_parser('obs', help='Get the list of observatories.')

    # subparser for getting the camera list
    parser_cam = subparsers.add_parser('cam', help='Get the list of cameras.')
    parser_cam.add_argument('--prefix', type=str, default=None, help='Prefix of the telescope/camera system.') # optional argument

    # subparser for generating a map
    parser_map = subparsers.add_parser('map', help='Generate a map of the observatories.')

    args = parser.parse_args()

    token = args.token
    prefix = args.prefix if hasattr(args, 'prefix') else None

    bhtasks = BHTasks(token)
    result = bhtasks.solve_for(parser)
    print(result)
