using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace gdscapp.ContentViews;

public partial class Folder : ContentView
{

    public Label FolderName
    {
        get => FolderNameLabel;
    }
    public VerticalStackLayout FileNamesLayout
    {
        get => FileNames;
    }
    public Folder()
    {
        InitializeComponent();
    }
}