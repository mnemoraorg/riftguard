package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"riftguard.mnemora.org/internal/api/router"
	"riftguard.mnemora.org/internal/config"
)

func main() {
	// 1. Load configuration
	cfg := config.LoadConfig()

	// 2. Setup router
	r := router.SetupRouter()

	// 3. Create server
	srv := &http.Server{
		Addr:         fmt.Sprintf(":%s", cfg.Port),
		Handler:      r,
		ReadTimeout:  15 * time.Second,
		WriteTimeout: 15 * time.Second,
	}

	// 4. Start server
	log.Printf("Starting [%s] server on port %s...", cfg.Env, cfg.Port)
	if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		log.Fatalf("listen: %s\n", err)
	}
}
