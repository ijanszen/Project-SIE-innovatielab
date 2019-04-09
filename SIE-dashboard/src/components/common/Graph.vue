<script>
import { Line } from 'vue-chartjs'
import $ from 'jquery'

export default {
    extends: Line,
    data() {
        return{
            datacollection: {
                //Data to be represented on x-axis
                labels: this.createLabel(120),
                datasets: this.retrieveDataSets()
            },
            //Chart.js options that controls the appearance of the chart
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            stacked: true
                        },
                        gridLines: {
                            display: true
                        }
                    }],
                    xAxes: [ {
                        gridLines: {
                            display: false
                        }       
                    }]
                },
                legend: {
                    display: true
                },
                responsive: true,
                maintainAspectRatio: false
            },
            settings: {
                "async": true,
                "crossDomain": true,
                "url": "https://api.beebotte.com/v1/data/read/NetAtmo/Co2?limit=4&source=raw&time-range=current-week",
                "method": "GET",
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": "WidakEvwajDNKL7BNVvHhqFI:lxX0Ov9YJOBxz6OUiJdcjWR+0og=",
                    "cache-control": "no-cache",
                    "Postman-Token": "bd2e8310-8b81-4d12-a293-32f0e191dd9e"
                },
                "processData": false,
                "data": ""
            }
        }
    },
    mounted() {
        // this.renderChart(this.datacollection, this.options)
    },
    methods: {
        firstMethod: function(api) {

            //Dit verhaal met URL en AUTH misschien niet wenselijk, is voor testdoeleinden
            var URL;
            var AUTH;
            if(api == "Co2") {
                URL = "https://api.beebotte.com/v1/data/read/NetAtmo/Co2?limit=120&source=raw&time-range=current-week"
                AUTH = "WidakEvwajDNKL7BNVvHhqFI:fj50MegQbZJsyGrm9lojvIDZLh4="
            } else if(api == "Noise") {
                URL = "https://api.beebotte.com/v1/data/read/NetAtmo/Noise?limit=120&source=raw&time-range=current-week"
                AUTH = "WidakEvwajDNKL7BNVvHhqFI:L0zee60Ugx28jiDBowWQlSDMapc="
            } else if(api == "Pressure") {
                URL = "https://api.beebotte.com/v1/data/read/NetAtmo/Pressure?limit=120&source=raw&time-range=current-week"
                AUTH = "WidakEvwajDNKL7BNVvHhqFI:vvbvZvbnfU0AYhFkXgN5IDIHhc8="
            }

            var list = [];
            $.ajax({
                "async": true,
                "crossDomain": true,
                "url": URL,
                "method": "GET",
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": AUTH,
                    "cache-control": "no-cache",
                    "Postman-Token": "bd2e8310-8b81-4d12-a293-32f0e191dd9e"
                },
                "processData": false,
                "data": ""
            }).done(function (response) {
                for (var i = 0; i < response.length; i++) {
                    list.push(response[i].data)
                }
            })
            setTimeout(() => {
                this.renderChart(this.datacollection, this.options)
            }, 1000);
            return list;
        },
        createLabel(num) {
            var interval = num / 4;
            var intervalCounter = 0;
            var labelList = []
            for( var i = 0; i < num; i++){
                if(i == 0) {
                    labelList.push("Label")
                }
                 if (intervalCounter >= interval -1) {
                    labelList.push("Label")
                    intervalCounter = 0;
                } else {
                    labelList.push("")
                    intervalCounter ++
                }
            }
            return labelList
        },
        retrieveDataSets() {
            //Dit is niet wenselijk op deze manier, was voor testdoeleinden
            var dataSet = [
                    {
                    radius: 0,
                    lineTension: 0,
                    fill: false,
                    label: 'Co2',
                    borderColor: 'blue',
                    pointBackgroundColor: 'white',
                    borderWidth: 2,
                    pointBorderColor: '#249EBF',
                    //Data to be represented on y-axis
                    data: this.firstMethod("Co2")
                    },{
                    radius: 0,
                    lineTension: 0,
                    fill: false,
                    label: 'Noise',
                    borderColor: '#b21901',
                    pointBackgroundColor: 'white',
                    borderWidth: 2,
                    pointBorderColor: '#249EBF',
                    //Data to be represented on y-axis
                    data: this.firstMethod("Noise")
                    },{
                    radius: 0,
                    lineTension: 0,
                    fill: false,
                    label: 'Pressure',
                    borderColor: 'green',
                    pointBackgroundColor: 'white',
                    borderWidth: 2,
                    pointBorderColor: '#249EBF',
                    //Data to be represented on y-axis
                    data: this.firstMethod("Pressure")
                    }
                ]
            return dataSet;
        }
    }
}



</script>
