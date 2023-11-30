using gdscapp.ContentViews;

namespace gdscapp;

public partial class ResultPage : ContentPage
{
    private readonly List<FolderInfo> _folderInfos = new();
    
    public ResultPage()
    {
        InitializeComponent();
        var folderInfo = new FolderInfo("こころのはたらき");
        folderInfo.Files.Add("第一回 授業説明.pdf");
        folderInfo.Files.Add("第二回.pdf");
        folderInfo.Files.Add("第三回.pdf");
        folderInfo.Files.Add("第四回.pdf");
        _folderInfos.Add(folderInfo);
        var folderInfo2 = new FolderInfo("日本学B");
        folderInfo2.Files.Add("第1回 授業説明.pdf");
        folderInfo2.Files.Add("第2回.pdf");
        folderInfo2.Files.Add("第3回.pdf");
        folderInfo2.Files.Add("第4回.pdf");
        _folderInfos.Add(folderInfo2);
        
        foreach (var i in _folderInfos)
        {
            var folderView = new Folder();
            folderView.FolderName.Text = i.Name;
            foreach (var file in i.Files)
            {
                folderView.FileNamesLayout.Add(new Label(){ Text = $"・ {file}" });
            }
            
            FolderLayout.Add(folderView);
        }
    }
}

public struct FolderInfo
{
    public FolderInfo(string name)
    {
        Name = name;
        Files = new();
    }
    
    public string Name { get; private set; }
    public List<string> Files { get; private set; }
}