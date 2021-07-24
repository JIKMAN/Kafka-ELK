## Logstash 설치하기

1. Install Public Signing Key 
* `wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -`

```
apt-key는 apt가 패키지를 인증하는 데 사용하는 키 목록을 관리하는 패키지입니다.

키를 사용하여 인증된 패키지는 신뢰할 수 있는 것으로 간주됩니다.
```

2. Install dependencies

You may need to install the apt-transport-https package on Debian before proceeding
* `sudo apt-get install apt-transport-https`

3. Add elastic search repository
* `echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list`
4. Update the apt repository
* `sudo apt-get update`
5. Install Logstash
* `sudo apt-get install logstash`

---
> ### Starting Logstash
