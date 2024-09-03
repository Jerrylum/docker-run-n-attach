# Docker Run and Attach Script

This Python script, `docker-run-n-attach.py`, provides a convenient way to run a Docker container and automatically attach to it using Visual Studio Code.

## Prerequisites

- Python 3
- Docker
- Visual Studio Code with the Remote - Containers extension installed

## Usage

1. Make sure the script is executable:

   ```
   chmod +x docker-run-n-attach.py
   ```

2. Run the script with the same arguments you would use for `docker run`:

   ```
   ./docker-run-n-attach.py [docker run arguments]
   ```

   For example:

   ```
   ./docker-run-n-attach.py --name my-container -v $(pwd):/workspace -it ubuntu:latest
   ```

3. The script will:
   - Run the Docker container with the provided arguments
   - Automatically open Visual Studio Code, connected to the newly created container

## How it works

1. The script passes all provided arguments to `docker run`.
2. It extracts the container name from the `--name` argument.
3. It then uses the Visual Studio Code command-line interface to open a new window connected to the container.

## Notes

- Make sure to include the `--name` argument when running the script, as it's used to identify the container for VS Code attachment.
- The script assumes that the container has a `/workspace` directory. Ensure your Docker image or run command sets this up correctly.

## Troubleshooting

If you encounter any issues:

- Ensure Docker is running and you have the necessary permissions.
- Check that the Remote - Containers extension is installed in VS Code.
- Verify that the container name is unique and not already in use.

For more information on using VS Code with containers, refer to the [official documentation](https://code.visualstudio.com/docs/remote/containers).
