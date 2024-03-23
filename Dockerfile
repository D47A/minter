FROM python:3.9.19-slim-bullseye as build

RUN apt update; apt install -y unzip xz-utils
COPY requirements.txt .
RUN pip install -r requirements.txt

## -----------------------

WORKDIR /miners
COPY fetch_miners.py .
RUN python fetch_miners.py

## -----------------------

WORKDIR /sphinx
COPY docs/ .
RUN sphinx-build -M html source/ build/

## -----------------------

FROM nginx:alpine as final
COPY --from=build /sphinx/build/html /nginx/html
COPY --from=build /miners/linux /nginx/html/linux
COPY --from=build /miners/windows /nginx/html/windows
COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]