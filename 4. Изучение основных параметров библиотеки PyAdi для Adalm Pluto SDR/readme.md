# Задание

1. При помощи приложения на Android\iOS - **WifiAnalyzer** найти работающие точки доступа на несущей частоте **2.4** [GHz];
2. Определить канал наиболее мощной из них. При помощи **Google** найти несущую частоту в данном канале;
3. Принять радиосигнал на несущей частоте выбранной точки доступа **WiFi**; Показать на графике.
    1. Графики подписать по имеющейся на данный момент информации. 
4. При подозрительной активности радиоканала зафиксировать “снимок” экрана с явными признаками передатчика. Проще говоря, визуально отличить шумы от передачи данных;

# Выполнение
1. Несущая точки доступа определялась по номеру канала в WifiAnalyzer. В исследуемом случае номер канала точки доступа - 11. Через интернет было установлено, что шестому каналу соответсвует несущая примерно 2.462 [GHz]
2. Точка доступа называлась Redmi Note 11 Pro
3. Скришнот: 
<details>
    <img src="https://github.com/100thKing/SDR_Practice/blob/main/4.%20%D0%98%D0%B7%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D1%85%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20PyAdi%20%D0%B4%D0%BB%D1%8F%20Adalm%20Pluto%20SDR/source/Wifi_analyzer.jpeg" 
    name = "Screenshot">
</details>
4. В результате выполнения программы были получены графики: 
<details>
  <img src="https://github.com/100thKing/SDR_Practice/blob/ece1f5ff16ee60942c1feb19db9aedd0bfa3981b/4.%20%D0%98%D0%B7%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D1%85%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20PyAdi%20%D0%B4%D0%BB%D1%8F%20Adalm%20Pluto%20SDR/source/1.jpeg" name="first">
  <img src="https://github.com/100thKing/SDR_Practice/blob/ece1f5ff16ee60942c1feb19db9aedd0bfa3981b/4.%20%D0%98%D0%B7%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D1%85%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20PyAdi%20%D0%B4%D0%BB%D1%8F%20Adalm%20Pluto%20SDR/source/2.jpeg" name="second">
  <img src="https://github.com/100thKing/SDR_Practice/blob/ece1f5ff16ee60942c1feb19db9aedd0bfa3981b/4.%20%D0%98%D0%B7%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D1%85%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20PyAdi%20%D0%B4%D0%BB%D1%8F%20Adalm%20Pluto%20SDR/source/3.jpeg" name="third">
  <img src="https://github.com/100thKing/SDR_Practice/blob/ece1f5ff16ee60942c1feb19db9aedd0bfa3981b/4.%20%D0%98%D0%B7%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D1%85%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20PyAdi%20%D0%B4%D0%BB%D1%8F%20Adalm%20Pluto%20SDR/source/4.jpeg" name="fourth">
</details>
