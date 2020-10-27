NON_CODE_DIRS_TO_MOUNT = []
SSS_NON_CODE_DIRS_TO_MOUNT = []
BRC_EXTRA_SINGULARITY_ARGS = []
BASE_CODE_DIR = '/global/home/users/jieq'
CODE_DIRS_TO_MOUNT = [
    BASE_CODE_DIR + '/railrl-private'
]
DIR_AND_MOUNT_POINT_MAPPINGS = [
    dict(
        local_dir=BASE_CODE_DIR + '/.mujoco/',
        mount_point='/root/.mujoco',
    ),
]
LOCAL_LOG_DIR = '/global/scratch/jieq/learning_data/'
OUTPUT_DIR_FOR_DOODAD_TARGET = '/tmp/doodad-output/learning_data'
# If not set, default will be chosen by doodad
# AWS_S3_PATH = 's3://bucket/directory
AWS_S3_PATH = 's3://llm-test'
# You probably don't need to change things below
# Specifically, the docker image is looked up on dockerhub.com.
DOODAD_DOCKER_IMAGE = 'gberseth/llm:latest'
INSTANCE_TYPE = 'c4.xlarge'
SPOT_PRICE = 0.05
GPU_DOODAD_DOCKER_IMAGE = 'gberseth/llm:latest'
GPU_INSTANCE_TYPE = 'g2.2xlarge'
GPU_SPOT_PRICE = 0.5
# These AMI images have the docker images already installed.
REGION_TO_GPU_AWS_IMAGE_ID = {
#     'us-west-1': "ami-874378e7",
#     'us-east-1': "ami-0ef1b374",
    'us-east-2': "ami-024f0e84c5a8282a8",
}
# This really shouldn't matter and in theory could be whatever
OUTPUT_DIR_FOR_DOODAD_TARGET = '/tmp/doodad-output/'
"""
Slurm Settings
"""
SINGULARITY_IMAGE = '/global/scratch/gberseth/ubuntu_llm.img'
SINGULARITY_PRE_CMDS = [
    'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mjpro150/bin'
]
SLURM_CONFIGS = dict(
    cpu=dict(
        account_name='fc_rail',
        partition='savio',
        n_gpus=0,
        max_num_cores_per_node=8,
        time_in_mins=1200, ### 20 hours 
 ),
    gpu=dict(
        account_name='co_rail',
        partition='savio3_2080ti',
        n_gpus=1,
        max_num_cores_per_node=8,
        n_cpus_per_task=2,
        time_in_mins=1440, ### 20 hours   
 ),
)
"""
Slurm Script Settings
These are basically the same settings as above, but for the remote machine
where you will be running the generated script.
"""
SSS_CODE_DIRS_TO_MOUNT = [
    '/global/home/users/vitchyr/git/railrl',
    '/global/home/users/vitchyr/git/multiworld',
    '/global/home/users/vitchyr/git/doodad',
]
SSS_DIR_AND_MOUNT_POINT_MAPPINGS = [
    dict(
        local_dir='/global/home/users/vitchyr/.mujoco',
        mount_point='/root/.mujoco',
    ),
]
SSS_LOG_DIR = '/global/scratch/gberseth/doodad-log'
SSS_IMAGE = '/global/scratch/vitchyr/singularity_imgs/railrl-vitchyr-v2.img'
SSS_RUN_DOODAD_EXPERIMENT_SCRIPT_PATH = (
    '/global/home/users/vitchyr/git/railrl/scripts/run_experiment_from_doodad.py'
)
SSS_PRE_CMDS = [
    'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/global/home/users/vitchyr/.mujoco/mjpro150/bin'
]
"""
GCP Settings
"""
GCP_IMAGE_NAME = 'railrl-torch-4-cpu'
GCP_GPU_IMAGE_NAME = 'railrl-torch4cuda9'
GCP_BUCKET_NAME = 'railrl-steven'
GCP_DEFAULT_KWARGS = dict(
    zone='us-west2-c',
    instance_type='n1-standard-4',
    image_project='railrl-private-gcp',
    terminate=True,
    preemptible=True,
    gpu_kwargs=dict(
        gpu_model='nvidia-tesla-p4',
        num_gpu=1,
    )
)
