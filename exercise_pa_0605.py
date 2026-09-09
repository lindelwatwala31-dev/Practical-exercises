function GET_STOCK_DATA(cell) {
  const sheet = SpreadsheetApp.getActiveSheet();

  let symbol;
  if (typeof cell === 'string') {
    if (cell.match(/^[A-Z]+[0-9]+$/)) {
      const range = sheet.getRange(cell);
      symbol = range.getValue();
    } else {
      symbol = cell;
    }
  } else {
    return [["Error: Reference a cell or enclose your string in quotation marks"]];
  }

  if (!symbol) {
    return [['Enter symbol in cell']];
  }

  symbol = symbol.toString().trim().toUpperCase();

  try {
    const url = `https://query1.finance.yahoo.com/v8/finance/chart/${symbol}`;
    const response = UrlFetchApp.fetch(url);
    const data = JSON.parse(response.getContentText());

    const meta = data.chart.result[0].meta;
    const currentPrice = meta.regularMarketPrice;
    const previousClose = meta.previousClose;
    const change = currentPrice - previousClose;

    return [
      [
        currentPrice,        // Column 1: Current Price
        change,              // Column 2: Price Change ($)
        previousClose        // Column 3: Previous Close
      ]
    ];

  } catch (e) {
    return [['Error', e.toString().substring(0, 50)]];
  }
}