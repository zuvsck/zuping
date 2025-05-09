# Zuping

Zuping is a simple command-line tool to perform continuous ping checks on network addresses.

## Installation

1. Download the repository or source code.
2. Run the `install.bat` script to automatically set up dependencies and install Zuping:

   ```cmd
   install.bat
   ```

## Usage

1. After installation, you can run Zuping directly in the terminal:

   ```cmd
   zuping <address or IP>
   ```

2. To stop Zuping, press `Ctrl + C`.

## Example

```cmd
zuping google.com
```

This will start a continuous ping check to the domain `google.com` and display the formatted response times.
