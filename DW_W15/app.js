//Data Process
var my_data_today = []
d3.csv('data/MessiRonaldo.csv', function(d) {
    return {
        season : d.Season,
        player : d.Player,
        ligaGoals : +d.Liga_Goals,
        ligaAsts : +d.Liga_Asts,
        ligaAps : +d.Liga_Aps,
        ligaMins : +d.Liga_Mins,
        clGoals : +d.CL_Goals,
        clAsts : +d.CL_Asts,
        clAps : +d.CL_Aps,
        clMins : +d.CL_Mins
    };
}).then(function(data){
    data.forEach(e => {
        my_data_today.push(e);
    });
});

console.log(my_data_today);
console.log(my_data_today.length);

var my_processed_data = [];
for(var i = 0; i< my_data_today.length;i++){
    console.log('lpm!');
    if(my_data_today[i].season == '2017-18'){
        console.log('hola');
        new_element = [
            {axis: 'Goals', value: my_data_today[i].ligaGoals},
            {axis: 'Asists', value: my_data_today[i].ligaAsts},
            {axis: 'Aps', value: my_data_today[i].ligaAps},
            {axis: 'Mins', value: my_data_today[i].ligaMins}
        ]
        my_processed_data.push(new_element)
    }
}
console.log(my_processed_data);

//SET UP DIMENSIONS
var margin = {top: 100, right: 100, bottom: 100, left: 100},
    width = Math.min(700, window.innerWidth - 10) - margin.left - margin.right,
    height = Math.min(width, window.innerHeight - margin.top - margin.bottom - 20);

var color = d3.scaleBand().range(["#EDC951","#CC333F","#00A0B0"]);

var radarChartOptions = {
    w: width,
    h: height,
    margin: margin,
    maxValue: 0.5,
    levels: 5,
    roundStrokes: true,
    color: color
};

//Call function to draw the Radar chart
RadarChart(".radarChart", my_processed_data, radarChartOptions);