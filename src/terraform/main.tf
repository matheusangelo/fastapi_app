terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "fsapp" {
  name         = "fsapp:latest"
  keep_locally = false
}

resource "docker_container" "fsapp" {
  image = docker_image.fsapp.image_id
  name  = "fs_container"
  ports {
    internal = 8080
    external = 8000
  }
}
