namespace gdscapp.Backend;

public class FileWatcher
{
    public static void Start(string path)
    {
        FileSystemWatcher watcher = new FileSystemWatcher();
        watcher.Path = path;
        watcher.NotifyFilter = NotifyFilters.FileName;
        watcher.Created += new FileSystemEventHandler(OnCreated);
        watcher.EnableRaisingEvents = true;
    }

    private static void OnCreated(object _, FileSystemEventArgs e)
    {
        PythonCaller.Call(e.FullPath);
    }
}
