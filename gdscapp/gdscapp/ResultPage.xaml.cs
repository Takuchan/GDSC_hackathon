using gdscapp.Backend;
using gdscapp.ContentViews;

namespace gdscapp;

public partial class ResultPage : ContentPage
{
    private readonly List<FolderInfo> _folderInfos = new();
    private readonly List<Button> _moveButtons = new();
    private readonly List<Button> _folderButtons = new();
    public ResultPage()
    {
        // PythonCaller.UpdateResult = UpdateResult;
        
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
            var button = new Button() { Text = "To", IsEnabled = false };
            button.Clicked += OnFolderButton;
            _folderButtons.Add(button);
            folderView.FolderNameLayout.Add(button);
            foreach (var file in i.Files)
            {
                var horizontalLayout = new HorizontalStackLayout() { Spacing = 10, Padding = 10 };
                horizontalLayout.Add(new Label(){ Text = $"・ {file}", VerticalOptions = LayoutOptions.Center});
                var moveButton = new Button() { Text = "Move" };
                moveButton.Clicked += OnMoveButton;
                horizontalLayout.Add(moveButton);
                _moveButtons.Add(moveButton);
                
                
                folderView.FileNamesLayout.Add(horizontalLayout);
            }
            
            FolderLayout.Add(folderView);
        }
    }


    public void UpdateResult(List<FolderInfo> folderInfos)
    {
        // FolderLayout.Clear();
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
    private void OnMoveButton(object? obj, EventArgs e)
    {
        //MoveButtonを無効化
        ChangeButtonListEnable(_moveButtons, false);
        ChangeButtonListEnable(_folderButtons, true);
        
        
    }
    
    private void OnFolderButton(object? obj, EventArgs e)
    {
        ChangeButtonListEnable(_moveButtons, true);
        ChangeButtonListEnable(_folderButtons, false);
    }

    private void ChangeButtonListEnable(List<Button> buttons, bool isEnabled)
    {
        foreach (var button in buttons)
        {
            button.IsEnabled = isEnabled;
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