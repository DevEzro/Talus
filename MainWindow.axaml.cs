using Avalonia.Controls;
using Avalonia.Input;
using System.Diagnostics;

namespace Talus;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    private void InputArea_KeyDown(object? sender, KeyEventArgs e)
    {
        // Verificar si el usuario presionó Enter
        if (e.Key == Key.Enter)
        {
            var inputBox = sender as TextBox;
            if (inputBox != null)
            {
                string command = inputBox.Text.Trim(); // Obtener el comando
                ExecuteCommand(command); // Ejecutar el comando
                inputBox.Text = ""; // Limpiar el área de entrada
            }
        }
    }

    private void ExecuteCommand(string command)
    {
        // Configurar el proceso para ejecutar el comando
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "powershell.exe",
                Arguments = $"/c {command}",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            }
        };

        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        string error = process.StandardError.ReadToEnd();
        process.WaitForExit();

        // Actualizar el área de salida
        OutputArea.Text += $"> {command}\n";
        if (!string.IsNullOrEmpty(output))
            OutputArea.Text += $"{output}\n";
        if (!string.IsNullOrEmpty(error))
            OutputArea.Text += $"{error}\n";
        OutputScrollViewer.ScrollToEnd();
    }
}