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

EXAMPLE - Alert prefecture name when clicked:

```javascript
$(target).japanMap({
    onSelect : function(data){
        alert(data.name);     // "北海道" (Hokkaido) will be shown on dialog when you click Hokkaido Island.
    }
});
```

## License

Japan Map is released under the [MIT License](http://opensource.org/licenses/MIT).
