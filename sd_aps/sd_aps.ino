#include <ESP8266WiFi.h>
#include <aREST.h>

// Cria uma instancia aREST
aREST rest = aREST();

// Parâmetros de conexão WIFI
const char* ssid = "Aps";
const char* password = "12345678";

// The port to listen for incoming TCP connections
#define LISTEN_PORT           80

// Cria um servidor
WiFiServer server(LISTEN_PORT);

// Variáveis a serem exibidas na API
int noise;

// Declaração de funçõea a serem executadas via API
int ledControl(String command);

void setup(void)
{
  // Inicia o serial
  Serial.begin(115200);

  // Inicializa as variáveis e as exibe na REST API
  noise = 0;
  rest.variable("noise",&noise);

  // Definição da função na API
  rest.function("led",ledControl);

  // Nome e identificador do dispositivo
  rest.set_id("1");
  rest.set_name("noise_esp8266");

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connectado");

  // Inicia o servidor
  server.begin();
  Serial.println("Servidor iniciado");

  // Exibe o IP na rede
  Serial.println(WiFi.localIP());
}

void loop() {
  while(true) {
    // Controla chamadas no REST
    noise = analogRead(D0);
    WiFiClient client = server.available();
    if (!client) {
      return;
    }
    while(!client.available()){
      delay(1);
    }
    rest.handle(client);
  }
}

// Função de ligar o LED
int ledControl(String command) {

  // Get state from command
  int state = command.toInt();

  digitalWrite(6,state);
  return 1;
}
