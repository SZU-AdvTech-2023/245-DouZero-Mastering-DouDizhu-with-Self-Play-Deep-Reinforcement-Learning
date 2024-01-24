import os
import subprocess

def evaluate_models(model_folder, landlord_up_model, landlord_down_model, gpu_device):
    try:
        # Get a list of all files in the model folder
        model_files = [f for f in os.listdir(model_folder) if f.endswith('.ckpt') and f.startswith('landlord_weight_')]

        for landlord_model in model_files:
            # Construct the full path to the landlord model
            landlord_model_path = os.path.join(model_folder, landlord_model)

            # Print the model being evaluated
            print(f"Evaluating model: {landlord_model}")

            # Run the evaluation command
            evaluation_command = (
                f"python3 evaluate.py "
                f"--landlord {landlord_model_path} "
                f"--landlord_up {landlord_up_model} "
                f"--landlord_down {landlord_down_model} "
                f"--gpu_device {gpu_device}"
            )

            # Execute the evaluation command in the terminal
            subprocess.run(evaluation_command, shell=True, check=True)
    except Exception as e:
        print('MyErrorAtStart:  %s' % e)

if __name__ == "__main__":
    # Replace these with your actual paths and GPU device
    model_folder_path = "douzero_checkpoints/douzero/"
    landlord_up_model_path = "baselines/sl/landlord_up.ckpt"
    landlord_down_model_path = "baselines/sl/landlord_down.ckpt"
    gpu_device = "2"

    # Call the function to evaluate all models in the folder
    evaluate_models(model_folder_path, landlord_up_model_path, landlord_down_model_path, gpu_device)
