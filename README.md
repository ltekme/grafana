# Grafana

My Grafana Stack

## Setup Openwrt

Reference from [https://grafana.com/grafana/dashboards/11147-openwrt/](https://grafana.com/grafana/dashboards/11147-openwrt/)

```sh
apk add prometheus-node-exporter-lua \
prometheus-node-exporter-lua-nat_traffic \
prometheus-node-exporter-lua-netstat \
prometheus-node-exporter-lua-openwrt \
prometheus-node-exporter-lua-wifi \
prometheus-node-exporter-lua-wifi_stations
```

```sh
cat <<EOF > /etc/config/prometheus-node-exporter-lua
config prometheus-node-exporter-lua 'main'
        option listen_interface 'lan'
        option listen_port '9100'
EOF
```

```sh
/etc/init.d/prometheus-node-exporter-lua restart
```

## Setup pve

[https://github.com/prometheus-pve/prometheus-pve-exporter](https://github.com/prometheus-pve/prometheus-pve-exporter)

## Setup Kuma

[https://github.com/louislam/uptime-kuma](https://github.com/louislam/uptime-kuma)

## Setup linux-iso

[https://github.com/esanchezm/prometheus-qbittorrent-exporter/tree/master](https://github.com/esanchezm/prometheus-qbittorrent-exporter/tree/master)