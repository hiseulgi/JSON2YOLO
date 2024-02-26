import argparse

# Import functions from json2yolo.py
from general_json2yolo import convert_coco_json


def main():
    """
    Converts COCO JSON format to YOLO format.

    This script provides a command-line interface for easy conversion.

    **Usage:**

    ```bash
    python coco_to_yolo.py --json_dir path/to/coco_json_files --use_segments

    # For converting COCO classes from 91 to 80 categories:
    python coco_to_yolo.py --json_dir path/to/coco_json_files --cls91to80

    # For default behavior (no segmentation, 91 classes):
    python coco_to_yolo.py --json_dir path/to/coco_json_files
    ```

    **Arguments:**

    - `--json_dir`: (Optional) Path to the directory containing JSON annotation files.
      If not provided, assumes the default location of "coco/annotations".
    - `--use_segments`: (Optional) Flag to include segmentation information in the output (for COCO only).
      Defaults to False.
    - `--cls91to80`: (Optional) Flag to convert COCO classes from 91 to 80 categories (for COCO only).
      Defaults to False.
    """

    parser = argparse.ArgumentParser(
        description="Convert COCO JSON format to YOLO format."
    )

    # Input arguments
    parser.add_argument(
        "--json_dir",
        type=str,
        default="coco/annotations",  # Provide default value
        help="Path to the directory containing JSON annotation files (default: %(default)s)",
    )
    parser.add_argument(
        "--use_segments",
        action="store_true",
        default=False,
        help="Include segmentation information in the output (for COCO only)",
    )
    parser.add_argument(
        "--cls91to80",
        action="store_true",
        default=False,
        help="Convert COCO classes from 91 to 80 categories (for COCO only)",
    )

    args = parser.parse_args()

    # Call the appropriate conversion function based on the source
    convert_coco_json(
        json_dir=args.json_dir,
        use_segments=args.use_segments,
        cls91to80=args.cls91to80,
    )

    print(f"Conversion completed. Output saved to 'new_dir' directory.")


if __name__ == "__main__":
    main()
