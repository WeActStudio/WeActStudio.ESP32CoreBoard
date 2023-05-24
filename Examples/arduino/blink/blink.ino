/*---------------------------------------
 - WeAct Studio Official Link
 - taobao: weactstudio.taobao.com
 - aliexpress: weactstudio.aliexpress.com
 - github: github.com/WeActTC
 - gitee: gitee.com/WeAct-TC
 - blog: www.weact-tc.cn
 ---------------------------------------*/

void setup() {
  Serial.begin(115200);
  
  digitalWrite(22, HIGH);
  pinMode(22, OUTPUT);
}

void loop() {
  digitalWrite(22, HIGH);
  delay(1000);
  digitalWrite(22, LOW);
  delay(1000);  

  Serial.println("Hello WeAct Studio!");
}
