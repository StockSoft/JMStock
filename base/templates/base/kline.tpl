{% extends "base/base.tpl" %}

{% block title %} K线图测试 {% endblock %} 

{% block content %}

<div class='container'>
    <h4>K线图测试</h4>
    <form class='form form-inline' action='javascript:showKLine();'>
        <div class='form-group'>
            <label for='code'>股票代码: </label>
            <input type='text' id='code' name='code' placeholder='600848' />
        </div>
        <div class='form-group'>
            <label for='ktype'>K线类型: </label>
            <select id='ktype' name='ktype'>
                <option value='D'>日K线</option>
                <option value='W'>周K线</option>
                <option value='M'>月K线</option>
                <option value='5'>5分钟K线</option>
                <option value='15'>15分钟K线</option>
                <option value='30'>30分钟K线</option>
                <option value='60'>60分钟K线</option>
            </select>
        </div>
        <input type='submit' class='btn btn-primary' value='显示'>
    </form>
    <div id='klineContainer' style="height: 400px; min-width: 310px">
    </div>
</div>

{% endblock %}

{% block js %}
<script src="/static/js/highstock.js"></script>
<script src="/static/js/modules/exporting.js"></script>

<script type='text/javascript'>
function showKLine(){
    var code = $('#code').val();
    var ktype = $('#ktype').val();
    var ktypeName = $('#ktype').find("option:selected").text();

    if (!code) {
        alert('请输入有效股票代码');
        return;
    }
    if (!ktype) {
        alert('请选择K线类型');
        return;
    }

    var jsonUrl = '/base/klinedata/' + code + '/' + ktype + '/';

    $.getJSON(jsonUrl).done(function (data) {

        // split the data set into ohlc and volume
        var ohlc = [],
        volume = [],
        dataLength = data.length,
        // set the allowed units for data grouping
        groupingUnits = [
            [ 'minute', [5] ],
        ],

        i = 0;

        if (dataLength < 1) {
            alert('暂时找不到指定股票（' + code + '）的' + ktypeName + '图数据');
            return;
        }
        var title = '' + ktypeName + '图-' + code;

        for (i; i < dataLength; i += 1) {
            console.log(data[i]);
            console.log(data[i]['fields']['timestr']) 
            console.log(data[i]['fields']['open']) 
            ohlc.push([
                data[i]['fields']['timestamp'], // the date
                data[i]['fields']['open'],
                data[i]['fields']['high'],
                data[i]['fields']['low'],
                data[i]['fields']['close']
            ]);

            volume.push([
                data[i]['fields']['timestamp'], // the date
                data[i]['fields']['volume'],
            ]);
        }


        // create the chart
        $('#klineContainer').highcharts('StockChart', {
            rangeSelector: {
                selected: 1
            },

            title: {
                text: title
            },

            yAxis: [{
                    labels: {
                        align: 'right',
                        x: -3
                    },
                    title: {
                        text: 'K线'
                    },
                    height: '60%',
                    lineWidth: 2
                },{
                    labels:{
                        align: 'right',
                        x: -3
                    },
                    title: {
                        text: '交易量'
                    },
                    top: '65%',
                    height: '35%',
                    offset: 0,
                    lineWidth: 2
                }
            ],

            series:[{
                    type: 'candlestick',
                    name: 'K线',
                    data: ohlc,
                    dataGrouping:{
                        units: groupingUnits
                    }
                }, {
                    type: 'column',
                    name: '量',
                    data: volume,
                    yAxis: 1,
                    dataGrouping: {
                        units: groupingUnits
                    }
                }
            ]
        });
    }).fail(function() {
        alert('暂时找不到指定股票（' + code + '）的' + ktypeName + '图数据');
    });
};

// $(showKLine);
</script>

{% endblock %}
