using System.Diagnostics;
using System.IO;

namespace gdscapp.Backend;

// TODO: 名前がイマイチなので変えたい
public static class PythonCaller
{
    private static readonly string PythonPath = "python";
    private static readonly string PythonScriptPath = "../MainProgram/process.py";

    public static Action<List<FolderInfo>> UpdateResult { get; set; }

    public static void Call(string filePath)
    {
        //PDFを取得
        var pdfFiles = Directory.GetFiles(SettingsPage.FolderPath, "*.pdf", SearchOption.AllDirectories);
        var pdfArgs = string.Join(" ", pdfFiles);
        
        var startInfo = new ProcessStartInfo(PythonPath)
        {
            Arguments = $"{PythonScriptPath} {SettingsPage.ClusterNum} {pdfArgs}",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            CreateNoWindow = true
        };
        var process = new Process()
        {
            StartInfo = startInfo,
        };
        process.Start();
        
        var reader = process.StandardOutput;
        //これ、たぶん一行目しか読めないから、繰り返し処理にすることを検討。
        while(reader.ReadLine() is string output)
        {
            var splitedResult = output.Split(",");
            // outputがどのような形式かでいい感じにする。
            var folderName = splitedResult[1];
            var fileName = splitedResult[2];
            
            File.Move(SettingsPage.FolderPath + fileName, SettingsPage.FolderPath + folderName + fileName);
        }
        
        process.WaitForExit();
        process.Close();
        
        // UpdateResult?.Invoke(new ());
    }
}