# Japan Map

It show clickable map of prefectures (or area) of Japan.

## Installation

Include the script after the jQuery library:

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="/path/to/jquery.japan-map.js"></script>
```

## Usage

Creating the clickable map of Japan:

```javascript
$(target).japanMap( options );
```

### EXAMPLE 1

* Alert prefecture name when clicking, please check `Example1.html` file in `examples` folder for more details.

```javascript
$(target).japanMap({
    onSelect : function(data){
        alert(data.name);     // "北海道" will be shown on dialog when you click Hokkaido Island.
    }
});
```

![2018-02-15 12 22 37](https://user-images.githubusercontent.com/8428372/36240212-05db87be-124b-11e8-8c6a-10858c1bfc7e.png)

### EXAMPLE 2.1
* Change definition of the areas. (e.g., color, hoverColor, and prefectures) We can group many prefectures into one area.
* Move Nansei islands to top left hand side corner of the map.
* Show prefectures' names.
* Change the width of the map.
* Change the font size (and color) of prefectures.

```javascript
var areas = [
    {"code": 1, "color":"#ca93ea", "hoverColor":"#e0b1fb", "prefectures":[1]},
    {"code": 2, "color":"#a7a5ea", "hoverColor":"#d6d4fd", "prefectures":[2]},
    {"code": 3, "color":"#84b0f6", "hoverColor":"#c1d8fd", "prefectures":[3]},
    {"code": 4, "color":"#7cdc92", "hoverColor": "#aceebb", "prefectures":[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]}
];

$("#map").japanMap(
    {
        areas: areas,
        movesIslands: true,
        showsPrefectureName: true,
        width: 800,
        fontSize: 12,
        fontColor: "#000000",
        onSelect:function(data){
            alert(data.name);
        },
    }
);
```

![2018-02-15 3 11 16](https://user-images.githubusercontent.com/8428372/36244764-823a7150-1262-11e8-8f1e-ba6ed882a456.png)

### EXAMPLE 2.2
* Group prefectures into areas.
* Move Nansei islands to top left hand side corner of the map.
* Show areas' names.
* Change the width of the map.
* Change the font size (and color) of prefectures.

```javascript
var areas = [
    {code : 1, name: "北海道地方", color: "#7f7eda", hoverColor: "#b3b2ee", prefectures: [1]},
    {code : 2, name: "東北地方",   color: "#759ef4", hoverColor: "#98b9ff", prefectures: [2,3,4,5,6,7]},
    {code : 3, name: "関東地方",   color: "#7ecfea", hoverColor: "#b7e5f4", prefectures: [8,9,10,11,12,13,14]},
    {code : 4, name: "中部地方",   color: "#7cdc92", hoverColor: "#aceebb", prefectures: [15,16,17,18,19,20,21,22,23]},
    {code : 5, name: "近畿地方",   color: "#ffe966", hoverColor: "#fff19c", prefectures: [24,25,26,27,28,29,30]},
    {code : 6, name: "中国地方",   color: "#ffcc66", hoverColor: "#ffe0a3", prefectures: [31,32,33,34,35]},
    {code : 7, name: "四国地方",   color: "#fb9466", hoverColor: "#ffbb9c", prefectures: [36,37,38,39]},
    {code : 8, name: "九州地方",   color: "#ff9999", hoverColor: "#ffbdbd", prefectures: [40,41,42,43,44,45,46]},
    {code : 9, name: "沖縄地方",   color: "#eb98ff", hoverColor: "#f5c9ff", prefectures: [47]},
];

$("#map").japanMap(
    {
        areas: areas,
        showsAreaName : true,
        movesIslands: true,
        width: 800,
        fontSize: 16,
        fontColor: "#000000",
        onSelect:function(data){
            alert(data.name);
        },
    }
);
```

![2018-02-15 3 24 52](https://user-images.githubusercontent.com/8428372/36245105-6c1c15f2-1264-11e8-924e-06233166d169.png)

## License

Japan Map is released under the [MIT License](http://opensource.org/licenses/MIT).
