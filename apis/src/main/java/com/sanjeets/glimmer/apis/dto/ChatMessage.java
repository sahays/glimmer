package com.sanjeets.glimmer.apis.dto;

import java.util.UUID;
import lombok.Data;

@Data
public class ChatMessage {
    private UUID sessionId;
    private String sender; // "USER" or "AI"
    private String content;
    private MessageType type;

    public enum MessageType {
        CHAT,
        JOIN,
        LEAVE,
        TYPING
    }
}
