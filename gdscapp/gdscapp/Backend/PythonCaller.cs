using System.Diagnostics;

namespace gdscapp.Backend;

// TODO: 名前がイマイチなので変えたい
public class PythonCaller
{
    private static readonly string PythonPath = "python";
    private static readonly string PythonScriptPath = "./topofchikin/hogehoge.py";
    
    public static void Call(string filePath)
    {
        ProcessStartInfo startInfo = new ProcessStartInfo(PythonPath)
        {
            Arguments = PythonScriptPath,
            UseShellExecute = false,
            RedirectStandardOutput = true,
        };
        Process process = new Process()
        {
            StartInfo = startInfo,
        };
        process.Start();
        
        StreamReader reader = process.StandardOutput;
        string? output = reader.ReadLine();
        
        process.WaitForExit();
        process.Close();
        
        // TODO: ここでoutputを使ってファイル移動する
    }
}