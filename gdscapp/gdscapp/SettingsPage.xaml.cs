using System.Text.RegularExpressions;
using CommunityToolkit.Maui.Alerts;
using CommunityToolkit.Maui.Core;
using CommunityToolkit.Maui.Storage;

namespace gdscapp;

public partial class SettingsPage : ContentPage
{
    private string _previousText = "";
    private readonly Regex _outnumRegex = new(@"[^\d]+$");
    
    public SettingsPage()
    {
        InitializeComponent();

        NumInput.Text = Preferences.Get("NumClusters", "");
        NowFolderName.Text = Preferences.Get("FolderPath", "");
    }

    private void OnTextChanged(object sender, EventArgs e)
    {
        Entry entry = (Entry)sender;
        entry.Text = _outnumRegex.Replace(entry.Text, string.Empty);
        
        Preferences.Set("NumClusters", entry.Text);
    }

    private async void OnClickPickFolderButton(object _, EventArgs e)
    {
        await PickFolder(new());
    }
    private async Task PickFolder(CancellationToken cancellationToken)
    {
        var result = await FolderPicker.Default.PickAsync(cancellationToken);
        if (result.IsSuccessful)
        {
            await Toast.Make($"The folder was picked: Name - {result.Folder.Name}, Path - {result.Folder.Path}", ToastDuration.Long).Show(cancellationToken);
            NowFolderName.Text = result.Folder.Path;
            Preferences.Set("FolderPath", result.Folder.Path);
        }
        else
        {
            await Toast.Make($"The folder was not picked with error: {result.Exception.Message}").Show(cancellationToken);
        }
    }
}