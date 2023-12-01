using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using CommunityToolkit.Maui.Alerts;
using CommunityToolkit.Maui.Core;
using CommunityToolkit.Maui.Storage;

namespace gdscapp;

public partial class SettingsPage : ContentPage
{
    private string _previousText = "";
    private readonly Regex _outnumRegex;
    
    public SettingsPage()
    {
        InitializeComponent();
        _outnumRegex = new(@"[^\d]+$");
    }

    private void OnTextChanged(object sender, EventArgs e)
    {
        Entry entry = (Entry)sender;
        entry.Text = _outnumRegex.Replace(entry.Text, string.Empty);
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
        }
        else
        {
            await Toast.Make($"The folder was not picked with error: {result.Exception.Message}").Show(cancellationToken);
        }
    }
}