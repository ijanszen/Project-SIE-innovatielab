<script>
import { Line } from 'vue-chartjs'
export default {
    extends: Line,
    data() {
        return{
        datacollection: {
          //Data to be represented on x-axis
          labels: ['Test 1', 'Test 2', 'Test 3', 'Test 4'],
          datasets: [
              {
                  label: 'Data One',
                  backgroundColor: '#f87979',
                  pointBackgroundColor: 'white',
                  borderWidth: 1,
                  pointBorderColor: '#249EBF',
                  //Data topo be represented on y-axis
                  data: [10, 20, 30, 40]
              },
              {
                  label: 'Data Two',
                  backgroundColor: '#f82132',
                  pointBackgroundColor: 'white',
                  borderWidth: 1,
                  pointBorderColor: '#249EBF',
                  //Data topo be represented on y-axis
                  data: [40, 30, 20, 10]
              }
          ]
        },   
        //Chart.js options that controls the appearance of the chart
        options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero: true
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
        }
      }
    },
    mounted() {
        this.renderChart(this.datacollection, this.options)
    }
}
</script>
