<?php

function respond(mixed $data, int $status = 200){
    http_response_code($status);
    header("Content-Type: application/json");
    die(json_encode($data));
}

$url = $_SERVER['REDIRECT_URL'];

switch($url)
{
    case '/api/public/version':
        respond(['version' => 2.0]);
    
    case '/api/internal/flag':
        respond(['flag' => getenv('FLAG')]);
        
    default:
        respond(['error' => 'not found'], 404);
}