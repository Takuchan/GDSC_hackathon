//
// using CommunityToolkit.Maui.Alerts;
// using Microsoft.Extensions.Hosting;
//
// namespace gdscapp.Backend.WindowsService;
//
// // このクラスをMAUIのDIに登録するのが不可能っぽい
// public class AppBackground : BackgroundService 
// {
//     protected override async Task ExecuteAsync(CancellationToken stoppingToken)
//     {
//         while (!stoppingToken.IsCancellationRequested)
//         {
//             await Toast.Make("テスト").Show(stoppingToken);
//             await Task.Delay(TimeSpan.FromMinutes(10), stoppingToken);
//         }
//     }
// }