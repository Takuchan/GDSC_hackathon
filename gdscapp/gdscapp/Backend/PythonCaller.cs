using System.Diagnostics;
using System.IO;

namespace gdscapp.Backend;

// TODO: 名前がイマイチなので変えたい
public static class PythonCaller
{
    private static readonly string PythonPath = "python";
    private static readonly string PythonScriptPath = "./topofchikin/hogehoge.py";

    public static Action<List<FolderInfo>> UpdateResult { get; set; }

    public static void Call(string filePath)
    {
        var startInfo = new ProcessStartInfo(PythonPath)
        {
            Arguments = PythonScriptPath,
            UseShellExecute = false,
            RedirectStandardOutput = true,
        };
        var process = new Process()
        {
            StartInfo = startInfo,
        };
        process.Start();
        
        var reader = process.StandardOutput;
        //これ、たぶん一行目しか読めないから、繰り返し処理にすることを検討。
        var output = reader.ReadLine();
        
        process.WaitForExit();
        process.Close();
        
        // TODO: ここでoutputを使ってファイル移動する
        // outputがどのような形式かでいい感じにする。
        var folderInfo = new FolderInfo();
        
        // System.IOにいるやつだからたぶんどのプラットフォームでも動く。
        foreach (var file in folderInfo.Files)
        {
            File.Move(filePath + file, folderInfo.Name + file);   
        }
        
        UpdateResult.Invoke(new ());
    }
}