# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
from image_processing import ImageProcessingAISearch
import logging
import random
import string
import re

logging.basicConfig(level=logging.INFO)


def deploy_config(arguments: argparse.Namespace):
    """Deploy the indexer configuration based on the arguments passed.

    Args:
        arguments (argparse.Namespace): The arguments passed to the script"""

    random_str = ''.join(random.choices(
        string.ascii_letters + string.digits, k=8))

    suffix = None if arguments.suffix == "None" else arguments.suffix
    prefix = f'ailabs-{random_str}' if arguments.prefix == "None" else arguments.prefix
    index_config = ImageProcessingAISearch(
        suffix=suffix,
        rebuild=arguments.rebuild,
        prefix=prefix,
        enable_page_by_chunking=arguments.enable_page_wise_chunking,
    )

    index_config.deploy()

    if arguments.rebuild:
        index_config.reset_indexer()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some arguments.")

    def alphanum_dash(value):
        if not re.match(r'^[A-Za-z0-9][A-Za-z0-9\-]+$', value):
            raise argparse.ArgumentTypeError(
                "Prefix must be alphanumeric or contain '-' only.")
        return value

    parser.add_argument(
        "--prefix",
        type=alphanum_dash,
        required=True,
        help="Prefix to be attached to indexer objects (alphanumeric or '-' only)",
    )
    parser.add_argument(
        "--rebuild",
        type=bool,
        required=False,
        help="Whether want to delete and rebuild the index",
    )
    parser.add_argument(
        "--enable_page_wise_chunking",
        type=bool,
        required=False,
        help="Whether to enable chunking by page in adi skill, if no value it will be False",
    )
    parser.add_argument(
        "--suffix",
        type=str,
        required=False,
        help="Suffix to be attached to indexer objects",
    )

    args = parser.parse_args()
    deploy_config(args)
