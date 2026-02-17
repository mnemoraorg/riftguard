import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from "@repo/ui/components"

export default function HomePage() {
  return (
    <div className="p-10 font-sans">
      <h1 className="mb-8 text-4xl font-bold">Welcome to RiftGuard</h1>
      <div className="max-w-md">
        <Accordion type="single" collapsible>
          <AccordionItem value="item-1">
            <AccordionTrigger>What is RiftGuard?</AccordionTrigger>
            <AccordionContent>
              RiftGuard predicts tsunamis by analyzing earthquake signals in real time.
            </AccordionContent>
          </AccordionItem>
          <AccordionItem value="item-2">
            <AccordionTrigger>How does it work?</AccordionTrigger>
            <AccordionContent>
              It spots dangerous patterns early, giving life-saving warnings before waves hit
              coastal areas.
            </AccordionContent>
          </AccordionItem>
        </Accordion>
      </div>
    </div>
  )
}
