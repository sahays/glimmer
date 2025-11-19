package com.sanjeets.glimmer.apis.controller;

import com.sanjeets.glimmer.apis.dto.ChatMessage;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;

@Controller
@RequiredArgsConstructor
@Slf4j
public class ChatController {

    private final SimpMessagingTemplate messagingTemplate;

    @MessageMapping("/chat.send/{sessionId}")
    public void sendMessage(@DestinationVariable String sessionId, @Payload ChatMessage chatMessage) {
        log.info("Received message from session {}: {}", sessionId, chatMessage.getContent());

        // 1. Broadcast user message back to topic (Ack) if needed, or assume frontend handles optimistic UI
        // For now, echo it back to confirm receipt
        messagingTemplate.convertAndSend("/topic/chat/" + sessionId, chatMessage);

        // 2. Simulate AI processing (Mock)
        try {
            Thread.sleep(1000);
            ChatMessage aiResponse = new ChatMessage();
            aiResponse.setSessionId(chatMessage.getSessionId());
            aiResponse.setSender("AI");
            aiResponse.setType(ChatMessage.MessageType.CHAT);
            aiResponse.setContent("I received your message: " + chatMessage.getContent());

            messagingTemplate.convertAndSend("/topic/chat/" + sessionId, aiResponse);

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            log.error("AI simulation interrupted", e);
        }
    }

    @MessageMapping("/chat.join/{sessionId}")
    public void joinSession(@DestinationVariable String sessionId, @Payload ChatMessage chatMessage) {
        log.info("User joined session: {}", sessionId);
        chatMessage.setType(ChatMessage.MessageType.JOIN);
        chatMessage.setSender("SYSTEM");
        chatMessage.setContent("User joined the session.");
        messagingTemplate.convertAndSend("/topic/chat/" + sessionId, chatMessage);
    }
}
