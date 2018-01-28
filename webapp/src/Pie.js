import React from 'react';
import ChartistGraph from 'react-chartist';
 
class Pie extends React.Component {
  constructor(props){
    super(props);
  }

  render() {
    var data = this.props.data;
    var type = this.props.chart_type;

    // var type = "Bar";
    return (
      <div>
        <ChartistGraph data={data} type={type} />
      </div>
    )
  }
}

export default Pie;
