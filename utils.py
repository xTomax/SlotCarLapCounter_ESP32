timetrack = """
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    .button {{
      background-color: #4CAF50;
      border: none;
      color: white;
      padding: 15px 25px;
      text-align: center;
      font-size: 16px;
      cursor: pointer;
    }}

    .button:hover {{
      background-color: green;
    }}
    * {{
        box-sizing: border-box;
    }}

    /* Create four equal columns that floats next to each other */
    .column {{
      float: left;
      width: 25%;
      padding: 10px;
    }}

    /* Clear floats after the columns */
    .row:after {{
      content: "";
      display: table;
      clear: both;
    }}

    /* Responsive layout - makes the four columns stack on top of each other instead of next to each other */
    @media screen and (max-width: 600px) {{
      .column {{
        width: 100%;
      }}
    }}
    </style>
</head>
<body>
    <h1>Welcome to GP Slot Ameixa</h1>  
    
        <a href="/data" class="button">Inserir dados</a>
        <a href="/reset" class="button">Reset</a>
        <a href="/start" class="button">Iniciar contagens</a>
        <p>Preparado: {ready}</p>
    
    <h2>Time Track {laps} Voltas</h2>
    <div class="row">
      <div class="column" style="background-color:#8ad3db;">
        <h2>{car1_name}</h2>
        <b>{car1_times}</b>
      </div>
      <div class="column" style="background-color:#9ddae1;">
        <h2>{car2_name}</h2>
        <b>{car2_times}</b>
      </div>
      <div class="column" style="background-color:#b1e2e7;">
        <h2>{car3_name}</h2>
        <b>{car3_times}</b>
      </div>
      <div class="column" style="background-color:#c4e9ed;">
        <h2>{car4_name}</h2>
        <b>{car4_times}</b>
    </div>
</div>
    
</body>
</html>
"""

datainput = """
<html>
<head>
    <style>
        input[type=text], select {
          width: 100%;
          padding: 12px 20px;
          margin: 8px 0;
          display: inline-block;
          border: 1px solid #ccc;
          border-radius: 4px;
          box-sizing: border-box;
        }

        input[type=submit] {
          width: 100%;
          background-color: #4CAF50;
          color: white;
          padding: 14px 20px;
          margin: 8px 0;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }

        input[type=submit]:hover {
          background-color: #45a049;
        }

        div {
          border-radius: 5px;
          background-color: #f2f2f2;
          padding: 20px;
        }
    </style>
</head>
<body>
    <div>
    <form action="/datain">
        <label for="laps">Insira Numero de voltas: </label>
        <input type="number" name="laps" id="laps" min="1" max="50"></input>
        </br>
        <label for="car1">Insira nome carro 1: </label>
        <input type="text" name="car1" id="car1"></input>
        
        <label for="car2">Insira nome carro 2: </label>
        <input type="text" name="car2" id="car2"></input>
        
        <label for="car3">Insira nome carro 3: </label>
        <input type="text" name="car3" id="car3"></input>
        
        <label for="car4">Insira nome carro 4: </label>
        <input type="text" name="car4" id="car4"></input>
        
        <input type="submit" value="Gravar">
    </form>    
    </div>
</body>
</html>
"""