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

EXAMPLE 1 - Alert prefecture name when clicking:

```javascript
$(target).japanMap({
    onSelect : function(data){
        alert(data.name);     // "北海道" will be shown on dialog when you click Hokkaido Island.
    }
});
```

![2018-02-15 12 22 37](https://user-images.githubusercontent.com/8428372/36240212-05db87be-124b-11e8-8c6a-10858c1bfc7e.png)


## License

Japan Map is released under the [MIT License](http://opensource.org/licenses/MIT).
