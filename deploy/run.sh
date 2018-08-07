echo "service running"

while :
do
	# 休眠30*24*3600，30天
	sleep 2592000
	hour=`date "+%H"`
	# 只在凌晨三点更新
	while [ $hour -ne 3 ]
	do
		# 休眠半小时
		sleep 1800
	done
	`/usr/bin/certbot renew --force-renewal`
	`/usr/sbin/service nginx restart`
	
	echo `date`
	echo 'update ssl'
done