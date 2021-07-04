import logging
import os
import os.path
import subprocess
import tarfile
from dataclasses import dataclass
from distutils.dir_util import copy_tree
from pathlib import Path

from google.cloud import storage

logger = logging.getLogger(__name__)


@dataclass
class SaveOutputToCloud:
    bucket_name: str

    def on_training_finished(self, training_project_name: str, output_dir: Path):
        try:
            path_to_file, file_name = self.make_tarfile(training_project_name, output_dir)
            self.upload_blob(path_to_file, file_name)
        except Exception as e:
            logger.error("Failed to save output to cloud", e)
            raise Exception("Failed to save output to cloud")

    def make_tarfile(self, training_project_name: str, output_dir: Path):
        tar_source_dir_path = output_dir.parent / training_project_name
        tar_file_name = training_project_name + '.tar.gz'
        tar_file_path = output_dir.parent / tar_file_name
        copy_tree(str(output_dir), str(tar_source_dir_path))

        with tarfile.open(tar_file_path, "w:gz") as tar:
            tar.add(str(tar_source_dir_path), arcname=os.path.basename(str(tar_source_dir_path)))

        return str(tar_file_path), tar_file_name

    def upload_blob(self, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        # destination_blob_name = "storage-object-name"

        storage_client = storage.Client()
        bucket = storage_client.bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        logger.info("File %s uploaded to %s.", source_file_name, destination_blob_name)


class DestroyVastAiInstance:

    def on_training_finished(self, this_vast_ai_instance_id, vast_ai_api_token):
        try:

            result = subprocess.run(
                ["vast", "destroy instance", str(this_vast_ai_instance_id), "--api-key",
                 vast_ai_api_token], capture_output=True, check=True)

            logger.info("Destroying this vast ai instance, returned: %s", str(result))

        except Exception as e:
            logger.error("Failed to destroy vast-ai instance", e)
