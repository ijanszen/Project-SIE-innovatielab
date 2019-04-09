<script>
import { Line } from 'vue-chartjs'
import $ from 'jquery'

export default {
    extends: Line,
    data() {
        return{
            datacollection: {
                //Data to be represented on x-axis
                labels: ["11:15","","", "11:30","","", "11:45","","", "12:00"],
                datasets: [
                    {
                    label: 'Data One',
                    backgroundColor: '#f87979',
                    pointBackgroundColor: 'white',
                    borderWidth: 1,
                    pointBorderColor: '#249EBF',
                    //Data to be represented on y-axis
                    data: this.firstMethod()
                    }
                ]
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
                        ticks: {
                            autoSkip: true,
                            maxTicksLimit: 20
                        },
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
        // $.ajax(this.settings).done(function (response) {
        //     var i = 0;
        //     var list = [];
        //     console.log(response);
        // })
        this.renderChart(this.datacollection, this.options)
    },
    methods: {
        firstMethod: function() {
            var list = [];
            $.ajax({
                "async": true,
                "crossDomain": true,
                "url": "https://api.beebotte.com/v1/data/read/NetAtmo/Noise?limit=120&source=raw&time-range=current-week",
                "method": "GET",
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": "WidakEvwajDNKL7BNVvHhqFI:L0zee60Ugx28jiDBowWQlSDMapc=",
                    "cache-control": "no-cache",
                    "Postman-Token": "bd2e8310-8b81-4d12-a293-32f0e191dd9e"
                },
                "processData": false,
                "data": ""
            }).done(function (response) {
                var i = 0;
                for (i; i < response.length; i++) {
                    list.push(response[i].data)
                }
            })
            setTimeout(() => {
                this.renderChart(this.datacollection, this.options)
            }, 3000);
            return list;
        }
    }
}



</script>
