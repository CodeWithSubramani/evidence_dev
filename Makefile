start:
	export NODE_TLS_REJECT_UNAUTHORIZED='0'
	python3 start.py
	npm run dev -- --host 0.0.0.0 --port 3001
	
	