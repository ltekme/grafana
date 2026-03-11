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

## Backup Up and Restore

'''sh
docker run -it \
-v grafana_grafana-storage:/grafana_grafana-storage:ro \
-v grafana_loki-storage:/grafana_loki-storage:ro \
-v grafana_prometheus-storage:/grafana_prometheus-storage:ro \
-v ./backups:/backup_dst \
ubuntu tar --same-owner -czvf /backup_dst/grafana.tar /grafana_grafana-storage /grafana_loki-storage /grafana_prometheus-storage
'''

'''sh
docker run -it \
-v grafana_grafana-storage:/grafana_grafana-storage:rw \
-v grafana_loki-storage:/grafana_loki-storage:rw \
-v grafana_prometheus-storage:/grafana_prometheus-storage:rw \
-v ./backups:/backup_dst:ro \
ubuntu \
bash -c "rm -rf /grafana_grafana-storage/* /grafana_prometheus-storage/* /grafana_prometheus-storage/* && tar --same-owner -xvf /backup_dst/grafana.tar -C /"
'''

