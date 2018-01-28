// var data = {
    //   labels: ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10'],
    //   series: [
    //     [1, 2, 4, 8, 6, -2, -1, -4, -6, -2]
    //   ]
    // };
    var data = {

      //my labels
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],

      //my multiple series
      series: [
        {
          //series1: label example: apples
          name: 'My nice apples',
          data: [5, 2, 4, 2, 0],
        },
        {
          //series1: label example: lemons
          name: 'My nice lemons',
          data: [8, 1, 14, 12, 10],
        },
        {
          //series1: label example: apples
          name: 'My nice apples',
          data: [5, 2, 4, 2, 0],
        }
      ]
    };
    var options = {
      // axisX: {
      //   labelInterpolationFnc: function(value, index) {
      //     return index % 2 === 0 ? value : null;
      //   }
      // }
    };
 
    var type = 'Line';

    // var pie_data = {
    //   labels: ['Bananas', 'Apples', 'Grapes'],
    //   series: [20, 15, 40]
    // };

    // var pie_options = [
    //   ['screen and (min-width: 640px)', {
    //     chartPadding: 30,
    //     labelOffset: 100,
    //     labelDirection: 'explode',
    //     labelInterpolationFnc: function(value) {
    //       return value;
    //     }
    //   }],
    //   ['screen and (min-width: 1024px)', {
    //     labelOffset: 80,
    //     chartPadding: 20
    //   }]
    // ];

    // var pie_type = 'Pie';
 