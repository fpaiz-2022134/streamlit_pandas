import streamlit as st
import streamlit.components.v1 as components

def show():
    st.title("Indicadores Principales X")

    html_code = """
    <style>
        body::-webkit-scrollbar {
            display: none;
        }
        body {
            overflow-y: auto;
        }

        .text-box {
            background: #f9f9f9;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: auto;
        }

        .image-box {
            text-align: center;
            margin-top: 30px;
        }

        .image-box img {
            width: 100%;
            max-width: 700px;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }

        h3 {
            color: #2c3e50;
            margin-bottom: 10px;
        }

        p, code {
            color: #333;
            line-height: 1.6;
            font-size: 16px;
            text-align: justify;
        }
    </style>

    <div class="text-box">
        <h1> Tasa de Victoria </h1>
        <h3>Descripción</h3>
        <p>Mide el porcentaje de victorias sobre el total de combates.</p>

        <h3>Método de cálculo</h3>
        <p><code>Win Rate = Wins / (Wins + Losses)</code></p>

        <h3>Justificación de importancia</h3>
        <p>Este indicador permite evaluar objetivamente la efectividad de un gladiador. 
        A diferencia del número bruto de victorias, la tasa considera también cuántas veces ha perdido, 
        ofreciendo así una métrica justa para comparar gladiadores con diferentes trayectorias. 
        Es esencial para identificar a los más exitosos y consistentes en la arena, 
        y sirve como base para predecir el rendimiento futuro.</p>



        <div class="image-box">
        <img src="https://i.guim.co.uk/img/media/384faecfbbc32859bc269b915a3f1fdeaa60a266/154_360_2795_1677/master/2795.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=059580cd4914df4339be6116c473ed0c" />
        </div>
        
        <h1> Condición Física Compuesta </h1>
        <h3>Descripción</h3>
        <p>Indica la calidad física integral del gladiador, combinando su altura, peso y estado de salud.</p>

        <h3>Método de cálculo</h3>
        <p><code>(Escala de Altura + Escala de Peso + Escala de Health Status) / 3</code></p>

        <h3>Justificación de importancia</h3>
        <p>Esta métrica ayuda a entender qué gladiadores están mejor preparados físicamente para 
        resistir los rigores del combate. Tener una buena condición física implica mayor fuerza, 
        aguante, agilidad y menor riesgo de lesiones. Este indicador es importante para anticipar 
        la ventaja física en un combate y para el diseño de entrenamientos más personalizados.
        También puede revelar desbalances entre condición física y rendimiento.</p>



        <div class="image-box">
        <img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/0*aetMV3H71yrXBs5c.jpg" />
        </div>
        
        <h1> Resiliencia Mental </h1>
        <h3>Descripción</h3>
        <p>Refleja la capacidad del gladiador para mantener la compostura emocional, superar la presión,
        y continuar luchando a pesar del miedo o la adversidad.</p>

        <h3>Método de cálculo</h3>
        <p><code>Valor directo del campo Mental Resilience, transformado en una escala cualitativa u ordinal 
        (Poor = 0, Moderate = 1, Strong = 2)./ 3</code></p>

        <h3>Justificación de importancia</h3>
        <p>La arena no es solo una prueba física, sino mental. Un gladiador con alta resiliencia es más resistente 
        al estrés y puede recuperarse emocionalmente después de derrotas o lesiones. Esta cualidad mejora la 
        constancia del rendimiento y minimiza errores bajo presión. También es útil para prever qué gladiadores 
        pueden durar más tiempo activos y liderar moralmente a otros.</p>



        <div class="image-box">
        <img src="https://nrtimes.co.uk/wp-content/uploads/2023/04/AdobeStock_584682858-1000x600.jpeg" />
        </div>
        
        <h1>Popularidad Pública</h1>
        <h3>Descripción</h3>
        <p>Mide el nivel de aceptación o carisma del gladiador frente al público, expresado como una puntuación entre 0 y 1.</p>

        <h3>Método de cálculo</h3>
        <p><code>Valor directo del campo Public Favor</code></p>

        <h3>Justificación de importancia</h3>
        <p>La popularidad puede cambiar el destino de un gladiador. Un público que apoya puede salvarlo tras una derrota, 
        exigir su presencia en eventos, y atraer mejores recursos, entrenadores y patrocinadores. Además, los gladiadores 
        populares son más rentables para sus dueños. Este indicador también sugiere la conexión emocional que genera un 
        luchador con la audiencia.</p>



        <div class="image-box">
        <img src="https://content.wkyc.com/photo/2016/11/10/USATSI_9494128_1478802183255_6996450_ver1.0.jpg" />
        </div>
        
        <h1>Experiencia de batalla</h1>
        <h3>Descripción</h3>
        <p>Representa el total de combates acumulados que ha tenido el gladiador, considerando victorias y derrotas.</p>

        <h3>Método de cálculo</h3>
        <p><code>Battle Experience (valor directo)</code></p>

        <h3>Justificación de importancia</h3>
        <p>La experiencia es clave para adquirir habilidades, enfrentar múltiples estilos y entender tácticas variadas.
        Gladiadores con mucha experiencia tienden a cometer menos errores y anticiparse mejor a las acciones del rival.
        Además, la experiencia correlaciona con la madurez profesional, siendo útil para identificar a veteranos estratégicos
        frente a novatos impulsivos.</p>



        <div class="image-box">
        <img src="https://ichef.bbci.co.uk/images/ic/1024xn/p0k63gxg.jpg.webp" />
        </div>
        
    </div>

    """

    components.html(html_code, height=900, scrolling=True)
    
    
