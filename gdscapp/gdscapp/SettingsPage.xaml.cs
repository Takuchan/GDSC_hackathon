using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

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
}