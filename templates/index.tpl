<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    .button {
      background-color: #4CAF50;
      border: none;
      color: white;
      padding: 15px 25px;
      text-align: center;
      font-size: 16px;
      cursor: pointer;
    }

    .button:hover {
      background-color: green;
    }
    
    
    * {
        box-sizing: border-box;
    }

    /* Create four equal columns that floats next to each other */
    .column {
      float: left;
      width: 25%;
      padding: 10px;
      height: 300px; /* Should be removed. Only for demonstration */
    }

    /* Clear floats after the columns */
    .row:after {
      content: "";
      display: table;
      clear: both;
    }

    /* Responsive layout - makes the four columns stack on top of each other instead of next to each other */
    @media screen and (max-width: 600px) {
      .column {
        width: 100%;
      }
    }
    </style>
</head>
<body>
    <h1>Welcome to GP Slot Ameixa</h1>  
    <a href="/data" class="button">Inserir dados</a>
    <a href="/reset" class="button">Reset</a>
    <h2>Time Track {laps} Voltas</h2>
    <div class="row">
      <div class="column" style="background-color:#aaa;">
        <h2>{car1_name}</h2>
        <p>{car1_times}</p>
      </div>
      <div class="column" style="background-color:#bbb;">
        <h2>{car2_name}</h2>
        <p>{car2_times}</p>
      </div>
      <div class="column" style="background-color:#ccc;">
        <h2>{car3_name}</h2>
        <p>{car3_times}</p>
      </div>
      <div class="column" style="background-color:#ddd;">
        <h2>{car4_name}</h2>
        <p>{car4_times}</p>
    </div>
</div>
    
</body>
</html>