<script>
import { Line } from 'vue-chartjs'
import $ from 'jquery'
import { setTimeout } from 'timers';

export default {
    extends: Line,
    props: ['API'],
    watch: {
        API: function(n, o) {
            //Iedere keer als de prop "API" een ander waarde krijgt zal er opnieuw data opgehaald worden via een API.
            //De juiste API-call wordt gemaakt op basis van de waarde van de prop "API". De waardes kunnen zijn: "Noise", "Co2", "Pressure", etc...
            this.datacollection = this.getDataCollection()
            // this.datacollection = {labels: this.createLabel(6, sessionStorage.getItem("dataNum")), datasets: this.getData(n)}
        }
    },
    data() {
        return{
            datacollection: this.getDataCollection(),
            // datacollection: {
            //     //Data to be represented on x-axis
            //     datasets: this.getData(this.$props.API),
            //     labels: this.createLabel(6, sessionStorage.getItem("dataNum"))
            // },
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
                        },
                        ticks: {
                            autoSkip: false
                        }
                    }]
                },
                legend: {
                    display: true
                },
                responsive: true,
                maintainAspectRatio: false
            }
        }
    },
    methods: {
        //Vue Chart.Js wil voor de grafiek een object met daarin de keys: 'datasets' en 'labels'
        getDataCollection() {
            var obj = {
                datasets: this.getData(this.$props.API),
              //  labels: this.createLabel(6, this.$props.dataNum)
            }
            
            setTimeout(() => {
                obj.labels = this.createLabel(6, obj.datasets[0].data.length)
                this.renderChart(this.datacollection, this.options)
            }, 1500);

            return obj
        },
        getData: function(api) {
            var URL = this.getUrlAndAuth(api).URL
            var AUTH = this.getUrlAndAuth(api).AUTH
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
                    "cache-control": "no-cache"
                },
                "processData": false,
                "data": ""
            }).done(function (response) {
                for (var i = 0; i < response.length; i++) {
                    sessionStorage.setItem("dataNum", response.length)
                    list.unshift(response[i].data)      
                }
            })

            var dataSet = {
                radius: 0,
                lineTension: 0,
                fill: false,
                label: api,
                borderColor: 'blue',
                pointBackgroundColor: 'white',
                borderWidth: 2,
                pointBorderColor: '#249EBF',
                //Data to be represented on y-axis
                data: list
            }
            return [dataSet]
        },

        getUrlAndAuth(api){
            var obj = {URL: null, AUTH: null}
            if(api == "Co2") {
                obj.URL = "https://api.beebotte.com/v1/data/read/NetAtmo/Co2?limit=720&source=raw&time-range=6hour"
                obj.AUTH = "WidakEvwajDNKL7BNVvHhqFI:Ei5JjEoeKVZ217l1FxCmWlwCLLY="
            } else if(api == "Noise") {
                obj.URL = "https://api.beebotte.com/v1/data/read/NetAtmo/Noise?limit=720&source=raw&time-range=6hour"
                obj.AUTH = "WidakEvwajDNKL7BNVvHhqFI:XU5YDRrAqbIUeLGDrTxTMmvuOFs="
            } else if(api == "Pressure") {
                obj.URL = "https://api.beebotte.com/v1/data/read/NetAtmo/Pressure?limit=720&source=raw&time-range=6hour"
                obj.AUTH = "WidakEvwajDNKL7BNVvHhqFI:z9lzz0FxbuKBTGvrm7eM6/BxQoU="
            } else if(api == "WiFi_stat") {
                obj.URL = "https://api.beebotte.com/v1/data/read/NetAtmo/WiFi_stat?limit=720&source=raw&time-range=6hour"
                obj.AUTH = "WidakEvwajDNKL7BNVvHhqFI:XR9HCBi709TUW8am7hpapPjPdwo="
            } else if(api == "Humidity") {
                obj.URL = "https://api.beebotte.com/v1/data/read/NetAtmo/Humidity?limit=720&source=raw&time-range=6hour"
                obj.AUTH = "WidakEvwajDNKL7BNVvHhqFI:3MqTOX2aiLfZQCNE3bDttZzWmls="
            } else if(api == "Temperature") {
                obj.URL = "https://api.beebotte.com/v1/data/read/NetAtmo/Temperature?limit=720&source=raw&time-range=6hour"
                obj.AUTH = "WidakEvwajDNKL7BNVvHhqFI:n1altpCduqLeEtEf4i6fGA3Ezu0="
            }
            return obj  
        },
        //Functie waarmee de labels voor de grafiek gegenereerd kunnen worden.
        //Het aantal datapunten en het aantal labels op de x-as moeten gelijk zijn, dus er moet een lijst gemaakt worden van labels.
        //Om de grafiek leesbaar te houden krijgen de meeste datapunten een lege string als label.
        //labelNum = het aantal labels dat je wilt hebben in de grafiek
        //dataNum = het aantal datapunten dat uit de api komt
        createLabel(labelNum, dataNum) {
            var interval = dataNum / labelNum;
            var intervalCounter = 0;
            var labelList = []

            var currentHour = new Date().getHours()

            for( var i = 0; i < dataNum; i++){
                if(i == 0 || intervalCounter >= interval -1) {
                    labelList.push(currentHour - labelNum)
                    intervalCounter = 0;
                    labelNum --
                } 
                else {
                    labelList.push("")
                    intervalCounter ++
                }
            }
            return labelList
        }
    }
}
</script>
