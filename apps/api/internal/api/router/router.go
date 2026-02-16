package router

import (
	"riftguard.mnemora.org/internal/api/handler"

	"github.com/gin-gonic/gin"
)

func SetupRouter() *gin.Engine {
	r := gin.Default()

	v1 := r.Group("/api/v1")
	{
		v1.GET("/hello", handler.HelloHandler)
	}

	return r
}
