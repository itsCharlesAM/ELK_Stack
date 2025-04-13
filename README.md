# 🔍🛠️📊 ELK Stack

## 🌍 Overview 
The **ELK Stack** is a powerful combination of tools designed for searching, analyzing, and visualizing log data in real-time. It is widely used for monitoring, log analysis, and data exploration. The stack consists of three core components: Elasticsearch, Logstash, and Kibana. Together, they provide an integrated solution for data ingestion, storage, and visualization.

### ELK stands for:
- **E**lasticsearch 🔍
- **L**ogstash 📥
- **K**ibana 📊

Each of these components serves a specific purpose in the stack.

## Components of ELK 🚀

### 1. **Elasticsearch** 🔍
Elasticsearch is a distributed search and analytics engine based on Apache Lucene. It is designed to handle large amounts of data in real time. Elasticsearch is commonly used for log or event data analysis and provides fast search capabilities, making it the heart of the ELK stack.

**Key Features**:
- Full-text search 📝
- Real-time data indexing and querying ⏱️
- Distributed and scalable 🌍

**How it works**:
- Data is ingested into Elasticsearch through various methods (e.g., Logstash, Beats, direct APIs).
- Elasticsearch indexes the data and makes it searchable through RESTful API queries.

### 2. **Logstash** 📥
Logstash is a server-side data processing pipeline that ingests data from multiple sources, transforms it, and then sends it to a "stash" like Elasticsearch. It can parse, filter, and enrich data in various formats.

**Key Features**:
- Real-time data processing ⏳
- Collects, parses, and transforms data from diverse sources 🌐
- Supports a wide variety of input, filter, and output plugins 🔌

**How it works**:
- Logstash collects log data from different sources.
- It processes and formats the data (such as converting log lines into structured JSON).
- After processing, the data is sent to Elasticsearch for indexing.

<img src="https://www.tatvasoft.com/blog/wp-content/uploads/2018/06/Data-Analytics-with-Elasticsearch-Logstash-and-Kibana-ELK.webp" alt="logstash_how_it_works" width="700"/>



### 3. **Kibana** 📊
Kibana is a visualization tool used to interact with the data stored in Elasticsearch. It provides real-time dashboards and visualizations for analyzing data, such as logs or metrics.

**Key Features**:
- Interactive visualizations (graphs, pie charts, maps, etc.) 📈
- Real-time (?) dashboards ⏱️
- Search and filtering capabilities 🔍
- Can be extended with plugins 🛠️

**How it works**:
- Kibana connects to Elasticsearch to visualize and query data.
- Users can create custom dashboards and visualizations to explore trends, patterns, and anomalies in their data.

## How to Run ELK Stack 🚀

### 1. **Install Elasticsearch** 🔍
To run Elasticsearch locally or on a server, you need to download and install it.

- Download from: https://www.elastic.co/downloads/elasticsearch
- Extract the archive and run Elasticsearch by executing:
  ```bash
  ./bin/elasticsearch.bat
  ```

  Elasticsearch will start on localhost on port 9200 by default (http://localhost:9200/)

  you can enable of disable security settting in `elasticsearch.yml` file (`config\elasticsearch.yml`)


### 2. **Install Kibana** 📊
Kibana is browser based interface that communicates with Elasticsearch.
  - Download from: https://www.elastic.co/downloads/kibana
  - Extract the archive and run Kibana:
  ```bash
  ./bin/kibana.bat
  ```


### 3. **Install Logstash** 📥
Logstash can be installed using the following steps.
  - Download from: https://www.elastic.co/downloads/logstash

  - the config file:
we must prepare a  `.conf`. this file is a pipeline and it has 3 main stages:
-input
-filter
-output
These stages define how Logstash collects, processes, and sends data to its final destination: Elasticsearch

```
input {
  file {
    path => "/path/to/logs/*.csv" (.log or anything)
    start_position => "beginning"
  }
}

filter {
  csv {
    separator => ","
    columns => ["first_name", "last_name", "address"]
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "index_name"  # we provide an index name for the log input data
  }

  stdout {}
}
```

  - Extract the archive and run Logstash with the configuration file:
  ```bash
  ./bin/logstash -f path_to_config_file.conf
  ```

You can see the `.conf` file I uploaded for my simple project.
I created a script that calls random user API and sends the response to a `.log` file with the format that I defined in `.conf` file and the script.
Then you can use the generated logs to test ELK services, like search API, monitoring the log data, etc.

Good luck! 🍀
