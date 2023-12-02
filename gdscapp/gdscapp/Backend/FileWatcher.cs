namespace gdscapp.Backend;

public static class FileWatcher
{
    private static FileSystemWatcher _watcher;
    public static void Start(string path)
    {
        _watcher?.Dispose();
        
        _watcher = new FileSystemWatcher();
        _watcher.Path = path;
        _watcher.NotifyFilter = NotifyFilters.FileName;
        _watcher.Created += OnCreated;
        _watcher.EnableRaisingEvents = true;
    }

    private static void OnCreated(object _, FileSystemEventArgs e)
    {
        PythonCaller.Call(e.FullPath);
    }
}
